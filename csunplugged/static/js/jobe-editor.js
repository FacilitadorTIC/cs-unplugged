// Scripts used to manage the UI functionality for the programming challenge editor screen.

const code_tester = require("./test-code.js");
var CodeMirror = require("codemirror");
require("codemirror/mode/python/python.js");

// Set up code mirror editor
let myTextarea = document.getElementById("codemirror_editor");
let myCodeMirror = CodeMirror.fromTextArea(myTextarea, {
  mode: {
    name: "python",
    version: 3,
    singleLineStringErrors: false
  },
  lineNumbers: true,
  textWrapping: false,
  styleActiveLine: true,
  autofocus: true,
  indentUnit: 4,
  viewportMargin: Infinity,
  // Replace tabs with 4 spaces. Taken from https://stackoverflow.com/questions/15183494/codemirror-tabs-to-spaces
  extraKeys: {
    Tab: function(cm) {
      cm.replaceSelection("    ", "end");
    }
  }
});

/**
 * Retrieves code from the code mirror editor, runs all the test cases then updates the results table.
 * Disables the "CHECK" button and shows a loading spinner while request is being processed.
 */
function sendCodeToJobe() {
  let code = myCodeMirror.getValue();

  $("#editor_run_button").prop("disabled", true);
  $(".code_running_spinner").css("display", "inline-block");

  code_tester.run_all_testcases(code, test_cases).then(result => {
    updateResultsTable(result);
    $("#editor_run_button").prop("disabled", false);
    $(".code_running_spinner").css("display", "none");
  });
}

/**
 * Updates the results table given some test case results.
 * @param {Array} results An array of test case results.
 */
function updateResultsTable(results) {
  for (result of results) {
    // Update status cell
    let status_element = $("#test-case-" + result.id + "-status");
    status_element.text(result.status);

    // Update output cell
    var output_element = $("#test-case-" + result.id + "-output");
    output_element.text(result.userOutput);

    // Update row colors
    var row_element = $("#test-case-" + result.id + "-row");
    if (result.status == "Passed") {
      row_element.addClass("table-success");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-warning");
    } else if (result.status == "Compiler Error") {
      row_element.addClass("table-warning");
      row_element.removeClass("table-danger");
      row_element.removeClass("table-success");
    } else {
      row_element.addClass("table-danger");
      row_element.removeClass("table-success");
      row_element.removeClass("table-warning");
    }
  }
}

// Setting up event listener for the check button to run the code.
let submitButton = document.getElementById("editor_run_button");
submitButton.addEventListener("click", sendCodeToJobe);
