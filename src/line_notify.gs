var ACCESS_TOKEN = "ここにアクセストークンを記入する"
var URL  = "https://notify-api.line.me/api/notify";

function line_notify(m){
  var options =
   {
     "method"  : "post",
     "payload" : {"message": m},
     "headers" : {"Authorization" : "Bearer "+ ACCESS_TOKEN}
   };
 
   UrlFetchApp.fetch(URL,options);
}
 
function line_notify_test(){
    line_notify("テストだよ");
}