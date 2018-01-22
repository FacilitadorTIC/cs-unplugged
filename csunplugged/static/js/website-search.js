$(document).ready(function() {
  $('#models-filter').multipleSelect({
    selectAll: false,
    width: '100%',
    placeholder: "Show all types",
  });

  $('#areas-filter').multipleSelect({
    filter: true,
    textTemplate: formatArea,
    selectAll: false,
    width: '100%',
    onClick: updateSelectedAreas,
    onOptgroupClick: updateSelectedAreas,
    maxHeight: 500,
  });

  // Render selected areas on initial load.
  updateSelectedAreas();

  // Add styling to <optgroup> labels.
  $('.areas-filter-container .ms-drop li.group').each(function(i, obj) {
    var data = areaData[$(this).next().find(':checkbox').val()];
    var label = $(this).find('label').contents().last();
    label.replaceWith(createAreaBadge(data.colour, label.text()));
  });

  // Indent all area children.
  $('.areas-filter-container .ms-drop li:not(.group)').find(':checkbox').each(function(i, obj) {
    if (areaData[$(this).val()]['child']) {
      $(this).addClass('area-child');
    }
  });

  // Clear form button.
  $('#clear-form').click(function(){
     $('#id_q').val('');
     $('#models-filter').multipleSelect('uncheckAll');
     $('#areas-filter').multipleSelect('uncheckAll');
 });
});

function createAreaBadge(colour, text) {
  /**
   * Create HTML of curriculum area badge.
   * @param {string} colour - Colour of badge.
   * @param {string} text - Text of badge.
   * @return {string} HTML of curriculum area badge.
   */
  return '<span class="area-badge badge-' + colour + '">' + text + '</span>';
};

function updateSelectedAreas(changeData) {
  /**
   * Update selected field with curriculum area badges.
   * @param {object} changeData - Data of the clicked item.
   */
  var $selectedSpan = $('.areas-filter-container .ms-choice span');
  $selectedSpan.empty();
  var $selectedValues = $('#areas-filter').multipleSelect('getSelects');
  if ($selectedValues.length == 0) {
    $selectedSpan.text("Show all curriculum areas");
  } else {
    for (var i = 0; i < $selectedValues.length; i++) {
      var data = areaData[$selectedValues[i]];
      $selectedSpan.append(createAreaBadge(data.colour, data.text));
    }
  }
};

function formatArea(element) {
  /**
   * Render curriculum area option in multiple select widget.
   * @param {Node} element - Element to render text.
   * @return {string} HTML of curriculum area badge.
   */
  var data = areaData[element[0].value];
  return createAreaBadge(data.colour, data.text);
};
