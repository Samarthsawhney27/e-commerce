export const ProductCard = ({ product }: { product: any }) => (
  <div className="glass-panel hover-lift" style={{ 
    padding: '1.5rem', 
    display: 'flex', 
    flexDirection: 'column', 
    gap: '1rem',
    height: '100%',
    justifyContent: 'space-between'
  }}>
    <div>
      <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>{product.name}</h3>
      <p style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--color-accent)' }}>
        ${product.price}
      </p>
    </div>
    <button className="btn btn-primary hover-glow" style={{ width: '100%' }}>
      Add to Cart
    </button>
  </div>
);
