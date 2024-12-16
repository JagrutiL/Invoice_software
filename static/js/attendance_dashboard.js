// DOM elements
const mainContent = document.getElementById('mainContent');
const navLinks = document.querySelectorAll('#navList a');
const tableRows = document.querySelectorAll('.table-container tbody tr'); // Adjust selector if needed
const sidebar = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebarToggle');
const closeSidebar = document.getElementById('closeSidebar');

// Sidebar Toggle Functionality
sidebarToggle.addEventListener('click', () => {
  sidebar.classList.toggle('show'); // Toggle sidebar visibility
  mainContent.classList.toggle('shift'); // Shift main content
});

closeSidebar.addEventListener('click', () => {
  sidebar.classList.remove('show'); // Hide sidebar
  mainContent.classList.remove('shift'); // Reset main content position
});

// Navigation Links Click Handling (for both Sidebar and Filtering)
navLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();  // Prevent default anchor behavior

    // Remove 'active' class from all links
    navLinks.forEach(nav => nav.classList.remove('active'));

    // Add 'active' class to the clicked link
    this.classList.add('active');
  });
});

// Initialize Date Picker on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  flatpickr("#dateRange", {
    mode: "range",
    dateFormat: "d/m/Y",
    onChange: (selectedDates) => {
      const [startDate, endDate] = selectedDates;  // Destructure dates
      console.log("Start Date:", startDate);
      console.log("End Date:", endDate);
    }
  });
});
// Initialize Date Picker on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  flatpickr("#dateRange", {
    mode: "range",
    dateFormat: "d/m/Y",
    onChange: (selectedDates) => {
      const [startDate, endDate] = selectedDates;  // Destructure dates
      console.log("Start Date:", startDate);
      console.log("End Date:", endDate);
    }
  });
});


const filterButton = document.getElementById('filterButton');
const filterList = document.getElementById('filterList');
const filterLinks = document.querySelectorAll('#filterList a');

// Toggle the visibility of the filter list
filterButton.addEventListener('click', (e) => {
  e.stopPropagation(); // Prevent click from closing immediately
  filterList.style.display = filterList.style.display === 'block' ? 'none' : 'block';
});
// Hide filter list when clicking outside
document.addEventListener('click', () => {
  filterList.style.display = 'none';
});
// Apply the filter when a filter link is clicked
filterLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent default anchor behavior

    const status = this.getAttribute('data-status'); // Get status from link

    // Filter table rows based on the selected status
    tableRows.forEach(row => {
      const rowStatus = row.getAttribute('data-status');
      row.style.display = (status === 'all' || rowStatus === status) ? '' : 'none';
    });

    filterList.style.display = 'none'; // Hide the dropdown after selection
  });
});