// ************************* tab swticher code start *************************

document.querySelectorAll('.admin_dashboard_attendance').forEach(admin_dashboard_attendance => {
    admin_dashboard_attendance.onclick = function () {
        document.querySelector('.admin_dashboard_attendance.admin_dashboard_selected')?.classList.remove('admin_dashboard_selected');
        this.classList.add('admin_dashboard_selected');
        document.querySelector('.target_current_switch_tab_working.active')?.classList.remove('active');
        document.getElementById(this.dataset.target).classList.add('active');
    };
});

// ************************* tab swticher code end *************************


// ****************** tab swticher code sidebar navar start ********************

const mainContent = document.getElementById('mainContent');
const navLinks = document.querySelectorAll('#navList a');
const tableRows = document.querySelectorAll('#invoiceTable tr');
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


// Add click event listener to each navigation link
navLinks.forEach(link => {
    link.addEventListener('click', function () {
        navLinks.forEach(nav => nav.classList.remove('active'));
        this.classList.add('active');
    });
});


// ****************** tab swticher code sidebar navar end********************
