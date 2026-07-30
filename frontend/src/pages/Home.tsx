import { useEffect, useState } from 'react';
import { ProductCard } from '../components/ProductCard';
import { fetchProducts } from '../services/api';

export const Home = () => {
  const [products, setProducts] = useState<any[]>([]);

  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);

  return (
    <div>
      <h2 className="page-title">Discover Our Products</h2>
      <p className="page-subtitle">Experience next-generation shopping with our meticulously crafted digital storefront. Browse our exclusive collection.</p>
      
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
        gap: '2rem' 
      }}>
        {products.map((p: any) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
};
