addEventListener("DOMContentLoaded", (e) => {
    const submitButton=document.querySelector('.btn');
    const question=document.querySelector(".question")
    const reponse=document.querySelector(".reponse")

    if (!submitButton){
        submitButton.addEventListener('click',(e)=>{
            if(!question&&!reponse){
                question.textContent="Chargement..."
                reponse.textContent="Chargement..."
            }
            
              
        })

    }
});
