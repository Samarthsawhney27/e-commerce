import { useEffect, useState } from 'react';
import { ProductCard } from '../components/ProductCard';
import { fetchProducts } from '../services/api';

export const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <div style={{ display: 'flex', gap: '1rem' }}>
        {products.map((p: any) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
};
