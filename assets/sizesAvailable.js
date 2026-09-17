var form = document.getElementById("CollectionFiltersForm");
if (form) {
  
  var addAvailability = () => {
    document.getElementById("Filter-Disponibilidad-1").checked = true;
  };

  $(".price-filter-range").on("click", function () {
    $("#filter-price-gte").val($(this).attr("data-lower-value"));
    $("#filter-price-lte").val($(this).attr("data-upper-value"));
    addAvailability();
    form.submit();
  });

  form.addEventListener("change", function () {
    addAvailability();
    form.submit();
  });
}
