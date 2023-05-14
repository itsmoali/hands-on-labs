
  // Write a function that will be called when the user clicks on the button

  var buttonHistory = ["Command History"];
  function showcommand(content) {
    var contentDiv = document.getElementById("contentDiv");
    buttonHistory.push(content);
    contentDiv.innerHTML = buttonHistory.join("<br>");
}