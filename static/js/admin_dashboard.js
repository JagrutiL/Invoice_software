document.querySelectorAll('.admin_dashboard_attendance').forEach(admin_dashboard_attendance => {
    admin_dashboard_attendance.onclick = function () {
        document.querySelector('.admin_dashboard_attendance.admin_dashboard_selected')?.classList.remove('admin_dashboard_selected');
        this.classList.add('admin_dashboard_selected');
        document.querySelector('.target_current_switch_tab_working.active')?.classList.remove('active');
        document.getElementById(this.dataset.target).classList.add('active');
    };
});
