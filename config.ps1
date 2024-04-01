param (
    [string]$FLASK_ENV,
    [string]$FLASK_APP
)

$env:FLASK_ENV = $FLASK_ENV
$env:FLASK_APP = $FLASK_APP