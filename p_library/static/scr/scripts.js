function init()  {
        const p_elements = document.querySelectorAll('form > p');

        p_elements.forEach(item => {
            item.classList.add("form-group")
        })

        const input_elements = document.querySelectorAll('form > p > input');

        input_elements.forEach(item => {
            item.classList.add("form-control")
        })

}

document.addEventListener("DOMContentLoaded", function(event) {
    init()
  });