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


//   // Add click event listener to each navigation link
//   navLinks.forEach(link => {
//       link.addEventListener('click', function () {
//           navLinks.forEach(nav => nav.classList.remove('active'));
//           this.classList.add('active');
//       });
//   });

document.addEventListener('DOMContentLoaded', () => {
    // Define navLinks
    const navLinks = document.querySelectorAll('.nav-link'); // Update selector as per your HTML structure
  
    // Ensure navLinks exist
    if (navLinks) {
      navLinks.forEach(link => {
        link.addEventListener('click', () => {
          navLinks.forEach(nav => nav.classList.remove('active'));
          link.classList.add('active');
        });
      });
    } else {
      console.error('No nav links found. Ensure you have elements with the "nav-link" class.');
    }
  });
  