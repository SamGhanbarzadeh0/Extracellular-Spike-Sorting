#!/usr/bin/env python3
"""Offline integrity verification for the 2026-11-22 spike-sorting results ZIP."""
from __future__ import annotations
import argparse,csv,hashlib,io,json,zipfile
from pathlib import Path

RUN_SHA = "57166309bf7c8c3a16032361cebb4a3af0ba3d1ac98da98ba89c6e31edd6822a"
EXPECTED = {"seed_stability.csv":45, "parameter_sensitivity.csv":270,
            "method_parameter_sensitivity.csv":70,"onset_alignment_sensitivity.csv":15,
            "polarity_sensitivity.csv":15,"reference_label_permutation_control.csv":10,
            "comparison.csv":45}

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as fp:
        for buf in iter(lambda: fp.read(1 << 20), b''):
            h.update(buf)
    return h.hexdigest()

def read_csv(archive: zipfile.ZipFile, name: str) -> list[dict[str,str]]:
    with archive.open(name) as stream:
        return list(csv.DictReader(io.TextIOWrapper(stream, encoding='utf-8')))

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--results-zip', type=Path, required=True)
    p.add_argument('--data-zip', type=Path)
    a=p.parse_args()
    got=digest(a.results_zip)
    assert got==RUN_SHA, f"Results SHA-256 mismatch: {got}"
    with zipfile.ZipFile(a.results_zip) as z:
        assert z.testzip() is None, 'Corrupt ZIP member'
        status=json.loads(z.read('FULL_VALIDATION_STATUS.json'))
        manifest=json.loads(z.read('RUN_COMPLETENESS_MANIFEST.json'))
        assert status['status']=='COMPLETE' and manifest['full_validation_completed']
        assert status['recordings']==[1,2,3,4,5] and status['methods']==9
        for n,num in EXPECTED.items():
            rows=read_csv(z,n)
            assert len(rows)==num, (n,len(rows),num)
            if n in status['tables']:
                assert status['tables'][n]==num
        for i in range(1,6):
            checkpoint=json.loads(z.read(f'_full_validation_checkpoints/simulation_{i}/COMPLETE.json'))
            assert checkpoint['status']=='COMPLETE'
            for table,count in checkpoint['stages'].items():
                rows=read_csv(z,f'_full_validation_checkpoints/simulation_{i}/{table}')
                assert len(rows)==count,(i,table,len(rows),count)
        for r in read_csv(z,'END_TO_END_HELDOUT_MICRO_SUMMARY.csv'):
            tp,fp,fn=(int(r[k]) for k in ('tp','fp','fn'))
            calc=(2*tp)/(2*tp+fp+fn)
            assert abs(calc-float(r['f1']))<1e-12
        if a.data_zip:
            with zipfile.ZipFile(a.data_zip) as source:
                assert source.testzip() is None
                for i in range(1,6):
                    data=source.read(f'data/simulation_{i}.mat')
                    digest_in_zip=hashlib.sha256(data).hexdigest()
                    assert digest_in_zip==manifest['source_checksums'][str(i)],i
    print('PASS: ZIP hash, completion, checkpoint counts, five-dataset results, and F1 arithmetic verified')

if __name__=='__main__':
    main()
