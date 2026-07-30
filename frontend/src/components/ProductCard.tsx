export const ProductCard = ({ product }: { product: any }) => (
  <div style={{ border: '1px solid #ccc', padding: '1rem' }}>
    <h3>{product.name}</h3>
    <p>${product.price}</p>
    <button>Add to Cart</button>
  </div>
);
