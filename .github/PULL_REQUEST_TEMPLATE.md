## Summary

What changed?

## Workflow impact

What user or maintainer workflow does this improve?

## Scope check

- [ ] Keeps the project focused on accompaniment workflows
- [ ] Does not overpromise Logic Pro automation
- [ ] Updates examples or documentation when prompt behavior changes
- [ ] Adds or updates tests when scripts change

## Verification

```bash
python3 -m compileall scripts tests
python3 -m unittest discover -s tests
```
