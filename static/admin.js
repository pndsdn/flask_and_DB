$(function () {
    var buttons = document.getElementsByClassName('buttons');
    var arr_but = [];
    for (i = 0; i < buttons.length; ++i) {
        arr_but[i] = buttons[i];
    }
    arr_but.forEach(function (e) {
        e.onclick = function(element) {
            element.preventDefault();
            var log_del = element.target.value;
            var request = { 'log-for-del': log_del }

            $.ajax({
                url: '/delete',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                dataType: 'json',
                data: JSON.stringify(request),
                success: function () {
                    window.location.assign("/admin/")
                }
            });
        }
    })
})
