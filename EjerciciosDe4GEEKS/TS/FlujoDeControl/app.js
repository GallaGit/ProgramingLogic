"use strict";
const posts = [
    { id: 1, content: "¡Hola mundo!", likes: 150, isSponsored: false },
    { id: 2, content: "¡Compra nuestro producto!", likes: 10, isSponsored: true },
    { id: 3, content: "Mira esto", likes: 75, isSponsored: false },
    { id: 4, content: "Contenido patrocinado", likes: 5, isSponsored: true },
    { id: 5, content: "Nuevo post viral", likes: 500, isSponsored: false },
    { id: 6, content: "Publicidad viral", likes: 1000, isSponsored: true }
];
const popularPosts = [];
const regularPosts = [];
const sponsoredPosts = [];
const zeroLikesPost = [];
for (let i = 0; i < posts.length; i++) {
    const post = posts[i];
    if (post.isSponsored) {
        // Las publicaciones patrocinadas van a su propio arreglo
        sponsoredPosts.push(post);
        continue; // Saltar las comprobaciones adicionales para publicaciones patrocinadas
    }
    // Para publicaciones no patrocinadas, categorizar según los likes
    if (post.likes === 0) {
        zeroLikesPost.push(post);
    }
    else if (post.likes >= 100) {
        popularPosts.push(post);
    }
    else {
        regularPosts.push(post);
    }
}
console.log("Publicaciones Populares:", popularPosts);
console.log("Publicaciones Regulares:", regularPosts);
console.log("Publicaciones Patrocinadas:", sponsoredPosts);
