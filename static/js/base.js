(function setBodyHeight() {
  function resetBodyHeight() {
    document.body.style.height = window.innerHeight + "px";
  }
  window.addEventListener("resize", resetBodyHeight);
  resetBodyHeight();
})();

(function initializeTooltips() {
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );
})();

$(document).ready(function () {
  $(".bs-multiselect").multiselect({
    includeSelectAllOption: true,
    buttonClass: "form-select",
    buttonWidth: "100%",
    buttonText: function (options, select) {
      if (options.length === 0) {
        return "--------";
      } else if (options.length > 1) {
        return `${options.length} selected`;
      } else {
        var labels = [];
        options.each(function () {
          if ($(this).attr("label") !== undefined) {
            labels.push($(this).attr("label"));
          } else {
            labels.push($(this).html());
          }
        });
        return labels.join(", ") + "";
      }
    },
    templates: {
      button:
        '<button type="button" class="multiselect dropdown-toggle d-block" data-bs-toggle="dropdown"><div class="multiselect-selected-text text-start"></div></button>',
    },
  });
});
