const express = require('express'); // import
const app = express(); // inicializando
const port = 3000;
const link = `https://localhost:${port}`

app.get('/', (req, res) => {
    res.send('Olá, minha imagem!');
});

app.listen(port, () => {
    console.log(`Executando na porta ${port}!`);
    console.log(`CTRL + click ${link}`);
})