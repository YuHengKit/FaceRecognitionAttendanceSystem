var myCalendar2;
var myCalendar;
var months = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct.', 'Nov.', 'Dec.'];

function sort() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
    onCalendarChange();
}
function sort1() {
  // Declare variables 
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search1");
  filter = input.value.toUpperCase();
  table = document.getElementById("table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}
function sort2() {
  // Declare variables 
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search2");
  filter = input.value.toUpperCase();
  table = document.getElementById("table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[4];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    } 
  }
}
function onCalendarChange() {
    var table, tr, td, i;
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");
    var fDate = new Date(myCalendar.getFormatedDate("%Y/%n/%j"));
    var lDate = new Date(myCalendar2.getFormatedDate("%Y/%n/%j"));
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[3].textContent;
        var year = td.split(' ')[2].split(',')[0];
        var month = td.split(' ')[0];
        var day = td.split(' ')[1].split(',')[0];
        var m = months.indexOf(month);
        var cDate = new Date(year,m,day);
        if (cDate <= lDate && cDate >= fDate && tr[i].style.display=="")
            tr[i].style.display = "";
        else
            tr[i].style.display = "none";
    }
}

$(function () {
    myCalendar = new dhtmlxCalendarObject("calendar");
    myCalendar2 = new dhtmlXCalendarObject("calendar2");
    myCalendar.attachEvent("onChange", sort);
    myCalendar2.attachEvent("onChange", sort);
});