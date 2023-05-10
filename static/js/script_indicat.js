// кнопка отправки на сервер


let btnResult = document.querySelector('.button__result')

btnResult.addEventListener('click', function (event) {

    // Проверяем правильность занесения данных
    indicateMistakes()

    if (statusRed == true ||
        (date_from.value == "" && date_until.value == "" && articul.value == "" && weight_from.value == "" && weight_until.value == "")) {

        // отменяет событие отправки данных с формы
        event.preventDefault();

        // заменая текста ответного сообщения
        trig = true
        let response_text = '<div class="response__btn">Проверьте правильность занесения параментров</div>'
        document.querySelector('.response__btn').outerHTML = response_text

        if  (document.querySelector('.response__btn').classList.contains('not_active')) {
            document.querySelector('.response__btn').classList.remove('not_active')
        }
    }

});

// Дата
let date_from= document.querySelector('[name="date_from"]')
let date_until = document.querySelector('[name="date_until"]')

// Артикул
let articul = document.querySelector('[name="articul"]')

// масса
let weight_from = document.querySelector('[name="weight_from"]')
let weight_until = document.querySelector('[name="weight_until"]')


// ДОЛЖЕН НАВЕСИТЬ ДРУГУЮ ФУНКЦИЮ В КОТОРОЙ СОДЕРЖИТСЯ indicateMistakes + СНЯТИЕ ОГРАНИЯЧЕНИЯ С СОБЫТИЯ
document.addEventListener("click", indicateMistakes);
date_from.addEventListener("click", indicateMistakes);
date_until.addEventListener("click", indicateMistakes);
articul.addEventListener("click", indicateMistakes);
weight_from.addEventListener("click", indicateMistakes);
weight_until.addEventListener("click", indicateMistakes);

function indicateMistakes() {

    statusRed = false

    testYear(date_from)
    testYear(date_until)

    testNumeric(articul)
    testNumeric(weight_from)
    testNumeric(weight_until)

};


function yellowColor(elem) {
    setColor(elem, '#FFFFE0')
}

function redColor(elem) {
    setColor(elem, '#FFD6D6')
    statusRed = true
}

function greenColor(elem) {
    setColor(elem, '#F0FFF0')
}

function whiteColor(elem) {
    setColor(elem, '#FFFFFF')
}

function setColor(elem, colorField) {
    elem.style.backgroundColor = colorField
    elem.parentNode.style.backgroundColor = colorField
    elem.parentNode.parentNode.style.backgroundColor = colorField
    /*elem.parentNode.parentNode.style.borderColor = colorBord*/
}

function testYear(elem) {

    // Проверка, что значение является целочисленным числом + годом

    if (Date.parse(elem.value) > 946684800000 && Date.parse(elem.value) < 1703980800000) {
        yellowColor(elem)
    } else if (elem.value === "") {
        whiteColor(elem)
    } else {
        redColor(elem)
    }
};


function testNumeric(elem) {

    // Проверка, что значение является целочисленным числом или плвающей точкой (без изменения фона окна)

//    let notDigit = false
//    let countAfterComma = null /*Number.isInteger(*/

    if (elem.value === "") {
        whiteColor(elem)
    } else if (typeof(parseInt(elem.value)) == 'number' && isNaN(elem.value) === false) {
        yellowColor(elem)
    } else {
        redColor(elem)
    }

};


document.getElementById('box').click()
