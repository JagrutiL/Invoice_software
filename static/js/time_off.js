document.addEventListener('DOMContentLoaded', function () {
    flatpickr("#dateRange", {
        mode: "range",
        dateFormat: "d/m/Y",  // You can adjust the format here
        onChange: function (selectedDates, dateStr, instance) {
            // This will trigger after selecting the date range
            const startDate = selectedDates[0];
            const endDate = selectedDates[1];
            console.log("Start Date:", startDate);
            console.log("End Date:", endDate);
        }
    });
});
