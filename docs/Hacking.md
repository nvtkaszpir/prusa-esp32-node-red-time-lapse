# Hacking

This assumes you have at least working docker-compose setup.
This also assumes you know how to alter existing code!

The code in version v1 was done in such way that:

- all in one flow (makes flow copies REALLY easier)
- it is easier to add additional printers (or cameras)
  as new flows or copy/paste fragments of flow
- it is easier to alter existing printer API parsing easier,
  just edit the `is printing?` node, especially if it returns JSON objects.

If you have ideas, please create new Issue, especially if you want to create PR.
