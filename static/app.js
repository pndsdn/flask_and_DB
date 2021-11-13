$(function () {
    const button = document.getElementById('button');
    button.onclick = function (e) {
        for (let i = 0; i < document.getElementsByClassName('input-value').length; ++i) {
            if (document.getElementsByClassName('input-value')[i].value == '') {
                e.preventDefault();
                document.getElementById("fill").classList.add("active");
                break;
            }
        }

    }

})