# How to Use This Plugin

This plugin can be used in a NOMAD Oasis installation.

## Add This Plugin to Your NOMAD installation

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/plugins/plugins.html#add-a-plugin-to-your-nomad) for all details on how to deploy the plugin on your NOMAD instance.

## How to use the LuQY Pro plugin

1. Prepare files
   - Ensure you have LuQY Pro measurement files (typically plain text `.txt` files).
   - Example files are available in the repository at: `src/nomad_luqy_plugin/example_uploads/getting_started`.

2. Upload in NOMAD
   - In the NOMAD web interface go to Publish -> Uploads.
   - Select the upload format / plugin named "LuQY Pro".
   - Upload one or more measurement files and fill required metadata (sample id, date, comments, ...).
   - Submit the upload.

3. What the plugin extracts
   - Scalar parameters: Laser intensity, Bias voltage, PLQY, QFLS, etc.
   - Spectral arrays: wavelength — intensity pairs.

4. View results
   - Open the Explore -> Measurements -> LuQY Pro to see parsed scalars and spectra.

5. Troubleshooting
   - If parsing fails, compare your files with the examples in `example_uploads`.
   - Inspect NOMAD worker / north logs for parser errors.

Notes
- The plugin must be installed on the NOMAD instance (see install instructions in this repository) before the "LuQY Pro" option appears in the upload dialog.