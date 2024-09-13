

function openModal(){
   const modal= document.querySelector('.modal')
   const modalwrap= document.querySelector('.modal_wrap')
   modal.classList.toggle('close')
   modalwrap.classList.toggle('close')
}

function closeModal(){
    const modal= document.querySelector('.modal')
    const modalwrap= document.querySelector('.modal_wrap')
    modal.classList.toggle('close')
    modalwrap.classList.toggle('close')
}