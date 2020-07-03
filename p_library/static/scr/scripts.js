() => {
    let elements = document.querySelectorAll('form p');
    console.log(elements);

    elements.forEach(item => {
        item.addClass("form-group")
    })
}