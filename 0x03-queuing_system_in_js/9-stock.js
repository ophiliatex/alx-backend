import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();

const reserveStockById = promisify(client.set).bind(client);
const getCurrentReservedStockById = promisify(client.get).bind(client);

const listProducts = [
    { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
    { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
    { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
    { id: 4, name: "Suitcase 1050", price: 550, stock: 5 }
];

function getItemById(id) {
    return listProducts.find(product => product.id === id);
}

app.get('/list_products', (req, res) => {
    const products = listProducts.map(({ id, name, price, stock }) => ({
        itemId: id,
        itemName: name,
        price,
        initialAvailableQuantity: stock
    }));
    res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
    const id = parseInt(req.params.itemId, 10);
    const product = getItemById(id);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getCurrentReservedStockById(`item.${id}`);
    const currentQuantity = product.stock - (parseInt(reservedStock, 10) || 0);

    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const id = parseInt(req.params.itemId, 10);
    const product = getItemById(id);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getCurrentReservedStockById(`item.${id}`);
    const currentQuantity = product.stock - (parseInt(reservedStock, 10) || 0);

    if (currentQuantity <= 0) {
        return res.json({
            status: 'Not enough stock available',
            itemId: id
        });
    }

    await reserveStockById(`item.${id}`, (parseInt(reservedStock, 10) || 0) + 1);

    res.json({
        status: 'Reservation confirmed',
        itemId: id
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
