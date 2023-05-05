let fieldDateSale = document.querySelector('[id="date_sale"]')
let fieldWeightFull = document.querySelector('[id="weight"]')


let stopClick = false

fieldDateSale.addEventListener('click', function() {
    fields_init_state()
    fields_open_state_object(fieldDateSale)
    event.stopImmediatePropagation()
})
fieldWeightFull.addEventListener('click', function() {
    fields_init_state()
    fields_open_state_object(fieldWeightFull)
    event.stopImmediatePropagation()
})

function fields_init_state() {

    // При клике на какой либо объект документа будет производится проверка
    // что нет двойного поля необходимого для закрытии

    // дата предложения
    fields_init_state_object(fieldDateSale)

    // стоимость полная
    fields_init_state_object(fieldWeightFull)

}


function fields_open_state_object(clickObject) {

    // увеличить поле ввода до поля с двойным внесением

    if (!clickObject.querySelectorAll('.input__parameter')[0].classList.contains('left_field_double') &&
        !clickObject.querySelectorAll('.input__parameter')[1].classList.contains('right_field_double')) {

        clickObject.querySelectorAll('.input__parameter')[0].classList.remove('left_field')
        clickObject.querySelectorAll('.input__parameter')[0].classList.add('left_field_double')

        clickObject.querySelectorAll('.input__parameter')[1].classList.remove('right_field')
        clickObject.querySelectorAll('.input__parameter')[1].classList.add('right_field_double')
    }
}


function fields_init_state_object(clickObject) {

    // вернуть поля ввода текста из увеличенного размера в обычное

    if (clickObject.querySelectorAll('.input__parameter')[0].classList.contains('left_field_double') &&
        clickObject.querySelectorAll('.input__parameter')[1].classList.contains('right_field_double')) {

        if (clickObject.querySelectorAll('.input__parameter')[0].querySelector('.value_input').value == '' &&
            clickObject.querySelectorAll('.input__parameter')[1].querySelector('.value_input').value == '') {

            clickObject.querySelectorAll('.input__parameter')[0].classList.remove('left_field_double')
            clickObject.querySelectorAll('.input__parameter')[0].classList.add('left_field')

            clickObject.querySelectorAll('.input__parameter')[1].classList.remove('right_field_double')
            clickObject.querySelectorAll('.input__parameter')[1].classList.add('right_field')
        }
    }
}

function openBox(idPrm) {

    let blockPrm = document.querySelector(`.${idPrm}`)
    let blockPrmArr = document.querySelectorAll(`.${idPrm}`)

    if (blockPrm.classList.contains('not_active')) {

        document.querySelectorAll(`.${idPrm}`).forEach(function(item) {

            item.style.border = "1px solid rgb(221, 160, 221)"
            item.style.background = "rgb(255, 255, 230)"
            item.classList.remove('not_active')

        })

        // Статус изменения кнопки появления фильтров
        statusSelectedBtn = true

    } else {

        let testEmpty = true

        document.querySelectorAll(`.${idPrm}`).forEach(function(item) {

            if (testEmpty == true) {

                item.querySelectorAll('input').forEach(function(it) {

                    if (it.value != "") {
                        testEmpty = False
                    }
                })
            }
        })

        if (testEmpty == true) {

            blockPrmArr.forEach(function(item) {
                item.classList.add('not_active')
            })

            statusSelectedBtn = false
            return false

        } else {
            statusSelectedBtn = true
        }
    }
    return true
}


function change_page(page) {

    let arr_numbers_page = document.querySelectorAll('.number_page')

    arr_numbers_page.forEach(function(item) {
        if (Number(item.innerText) == page) {
            document.querySelector(`[id="name_page"]`).innerHTML = '<input type="text" visibility="hidden" name="page" value="' + page + '" />'
        }
    })
}


function hideCorrect(idName, btnName) {
    if (!document.querySelector(`[id="${idName}"]`).classList.contains('not_active')) {
        let coords = document.querySelector(`[id="${btnName}"]`).getBoundingClientRect();
        document.querySelector(`[id="${idName}"]`).style.top = coords.bottom + 10 + "px";
        return;
    }
}


//// объект кнопки "выгрузка на сайт"
//let btnSite = document.querySelector('#site')
//
//// объект кнопки "выгрузка в excel"
//let btnExcel = document.querySelector('#excel')
//
//// объект input - сайт
//let inputSite = document.querySelector('#radio_site')
//
//// объект input - excel
//let inputExcel = document.querySelector('#radio_excel')
//
//
//btnSite.addEventListener("click", function() {
//    inputSite.click()
//});
//
//btnExcel.addEventListener("click", function() {
//    inputExcel.click()
//});



document.addEventListener("click", fields_init_state);

