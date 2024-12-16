  // DOM elements
  const mainContent = document.getElementById('mainContent');
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