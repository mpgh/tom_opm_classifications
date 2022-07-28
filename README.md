# tom_classifications

Classifications!

This is an app designed to support different ways a broker can classify a target using the TOM

The documentation and a more detailed readme will come later.


## Installation Procedure

1. Install the package into your TOM environment:

"pip install tom_classifications"

2. Migrate your TOM's database to install the new database tables:
`./manage.py migrate`

3. In your project's "settings.py", add "tom_classifications" to your "INSTALLED_APPS" setting:
"INSTALLED_APPS = [
    ...
    'tom_classifications',
]"

4. Copy the data files from "tom_classifications/data" to the data/ directory of your TOM.

5. Copy the target_detail.py into your TOM:
`cp tom_classifications/tom_classifications/templates/tom_targets/target_detail.html  [PATH]/mytom/templates/tom_targets/target_detail.html`
