document.addEventListener('DOMContentLoaded', function () {
    flatpickr("#dateRange", {
      mode: "range",
      dateFormat: "d/m/Y",
      onChange: function(selectedDates, dateStr, instance) {
        const startDate = selectedDates[0];
        const endDate = selectedDates[1];
        console.log("Start Date:", startDate);
        console.log("End Date:", endDate);
      }
    });
  });