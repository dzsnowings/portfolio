
var first = document.querySelector('.first-js');
var last = document.querySelector('.last-js');
var amount = document.querySelector('.principal-js');
var rate = document.querySelector('.rate-js');
var years = document.querySelector('.years-js');
var months = document.querySelector('.periods-js');
var button = document.querySelector('.button-js');
var output = document.querySelector('output');
var futurevalue = function(a, r, m, y) {
  var value = a * Math.pow(1 + (r / m), (y * m));
  return value;
};

button.addEventListener('click', function() {
  var fn = first.value;
  var ln = last.value;
  var a = parseFloat(amount.value);
  var r = parseFloat(rate.value);
  var m = parseFloat(months.value);
  var y = parseFloat(years.value);
  var result = futurevalue(a, r, m, y);
  var e = result - a;
  var output = "Congratulations, " + fn + " " + ln + "! \nThe future value of your investment = " + "$" + result.toFixed(2) + ".\nThat's $" + e.toFixed(2) + " in interest earned!";
  $("textarea#MyOutput").val(output);
});