

async function getData(){
    response = await axios.get("/api/cupcakes")
    return response
}

async function appendCupcakes(){
   data = await getData()
   cupcakes = data.data.cupcakes
   return cupcakes.forEach(function(c){
      return $('#cupcake-list').append(`
        <div data-id=${c.id} class = "card mt-2" style= "width: 18rem;">
            <img src="${c.image}" class="car-img-top">
            <div class="card-body">
                <h5 class="card-title">
                ${c.flavor.toUpperCase()}
                </h5>
                <h6 class="card-subtitle mb-2 text-muted">
                Size:${c.size}</h6>
                <h6 class="card-subtitle mb-2 text-muted">
                Size:${c.rating}</h6>
                <btn data-id=${c.id}  class="btn btn-link p-0">remove</btn>
            </div>
            
       </div>
        `)
   })
   
}




$('#sub-btn').click(async function(){
    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()
    
    let newCupcake = await axios.post('/api/cupcakes',{flavor,size,rating,image})
    location.reload()
})




$('#cupcake-list').on('click','btn', async function(evt){
    
     cupcake = $(evt.target).data('id')
    await axios.delete(`/api/cupcakes/${cupcake}`)
    location.reload()
    
})






appendCupcakes()