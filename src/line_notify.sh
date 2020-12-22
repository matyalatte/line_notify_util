token='token here'
curl -X POST -H "Authorization: Bearer "$token -F "message=$1" https://notify-api.line.me/api/notify
echo;