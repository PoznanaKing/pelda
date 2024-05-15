document.addEventListener('DOMContentLoaded', function () {
    // element-one: Hozzáad egy "box1style" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
    elementOne.onclick=function(event){
        elementOne.classList.add("box1style")
    }
    // element-two: Dupla kattintásra hozzáad egy 2px-es, fekete keretet
    const elementTwo = document.getElementById('element-two');
    elementTwo.ondblclick=function(){
            elementTwo.classList.add('box2style')
        }

    // element-three: Ha rámegy az egér, eltűnik
    const elementThree = document.getElementById('element-three');
        elementThree.onmouseover=function(){
            elementThree.classList.add('hidden')
        }
    // element-four: Kattintásra a szövegszín piros lesz benne
    const elementFour = document.getElementById('element-four');
    elementFour.onclick=function(){
        elementFour.style.color="red"
    }

    // Input mező: Billentyű lenyomásra az inputmező háttérszíne szürke lesz
    const inputField = document.getElementById('myInput');
    inputField.onkeydown=function(){
        if (inputField.innerHTML.value!=""){
            inputField.classList.add('inputmezo')
        }
        else{
            inputField.classList.remove('inputmezo')
        }
    }
});