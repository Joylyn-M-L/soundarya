import React, { useState } from 'react';

function App() {
  const [plaintext, setPlaintext] = useState('');
  const [aesResult, setAesResult] = useState(null);
  const [desResult, setDesResult] = useState(null);

  const handleEncrypt = async () => {
    const aesResponse = await fetch('http://localhost:8000/encrypt_aes/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plaintext }),
    });
    const aesData = await aesResponse.json();
    setAesResult(aesData);

    const desResponse = await fetch('http://localhost:8000/encrypt_des/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plaintext }),
    });
    const desData = await desResponse.json();
    setDesResult(desData);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>AES vs DES Encryption Demo</h1>
      <input
        type="text"
        placeholder="Enter text"
        value={plaintext}
        onChange={(e) => setPlaintext(e.target.value)}
        style={{ width: '300px', padding: '8px', marginBottom: '10px' }}
      />
      <br />
      <button onClick={handleEncrypt} style={{ padding: '10px 20px', marginBottom: '20px' }}>
        Encrypt
      </button>

      {aesResult && (
        <div style={{ marginBottom: '20px' }}>
          <h2>AES</h2>
          <p><strong>Ciphertext (Hex):</strong> {aesResult.ciphertext}</p>
          <p><strong>Time Taken (ms):</strong> {aesResult.time_taken}</p>

          <p><strong>Decrypted:</strong> {aesResult.decrypted}</p>
        </div>
      )}

      {desResult && (
        <div>
          <h2>DES</h2>
          <p><strong>Ciphertext (Hex):</strong> {desResult.ciphertext}</p>
          <p><strong>Time Taken (ms):</strong> {desResult.time_taken}</p>

          <p><strong>Decrypted:</strong> {desResult.decrypted}</p>
        </div>
      )}
    </div>
  );
}

export default App;


