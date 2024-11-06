# Vals AI Github Action

This is the repo for the Vals AI Github action. You can use it in your workflows like so:

```yaml:
steps:
      - uses: vals-ai/valsai-github-action@v0.0.20
        with:
          vals_api_key: ${{ secrets.VALS_API_KEY }}
          # TODO: Replace this with your own suite, or read from a configuration / environment variable.
          suite_link: "https://www.platform.vals.ai/view?test_suite_id=<SUITE ID>"
```
