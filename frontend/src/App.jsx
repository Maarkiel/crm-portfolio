import { useEffect, useState } from "react";

function App() {
  const [clients, setClients] = useState([]);
  const [selectedClient, setSelectedClient] = useState(null);
  const [interactions, setInteractions] = useState([]);
  const [note, setNote] = useState("");

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    status: ""
  });

  useEffect(() => {
    fetch("http://localhost:5000/clients")
      .then(res => res.json())
      .then(setClients);
  }, []);

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:5000/clients", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    })
      .then(() => {
        setFormData({ name: "", email: "", phone: "", status: "" });
        return fetch("http://localhost:5000/clients");
      })
      .then(res => res.json())
      .then(setClients);
  };

  const selectClient = (client) => {
    setSelectedClient(client);
    fetch(`http://localhost:5000/interactions/${client.id}`)
      .then(res => res.json())
      .then(setInteractions);
  };

  const handleAddNote = () => {
    fetch("http://localhost:5000/interactions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        client_id: selectedClient.id,
        note,
        interaction_date: new Date().toISOString()
      })
    })
      .then(() => {
        setNote("");
        return fetch(`http://localhost:5000/interactions/${selectedClient.id}`);
      })
      .then(res => res.json())
      .then(setInteractions);
  };

  return (
    <div className="min-h-screen bg-cover bg-center" style={{
      backgroundImage: "url('https://images.unsplash.com/photo-1532298488760-970ff6decf61?auto=format&fit=crop&w=1740&q=80')"
    }}>
      <div className="bg-black/60 min-h-screen px-6 py-12">
        <header className="text-center mb-12">
          <h1 className="heading-modern">⚒️ CRM Prototype v0.0.1</h1>
          <p className="text-gray-300">Zarządzaj klientami i notatkami z poziomu prototypu.</p>
        </header>

        <section className="card-modern max-w-5xl mx-auto">
          <h2 className="subheading-modern">Dodaj klienta</h2>
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <input name="name" value={formData.name} onChange={handleChange} placeholder="Imię i nazwisko" className="input-modern" required />
            <input name="email" value={formData.email} onChange={handleChange} placeholder="Email" className="input-modern" />
            <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Telefon" className="input-modern" />
            <input name="status" value={formData.status} onChange={handleChange} placeholder="Status" className="input-modern" />
            <div className="md:col-span-4">
              <button type="submit" className="btn-modern w-full">➕ Dodaj klienta</button>
            </div>
          </form>
        </section>

        <section className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="card-modern">
            <h2 className="subheading-modern">📋 Lista klientów</h2>
            <ul>
              {clients.map(client => (
                <li
                  key={client.id}
                  onClick={() => selectClient(client)}
                  className="list-item"
                >
                  <div className="flex justify-between items-center">
                    <div>
                      <strong>{client.name}</strong><br />
                      <span className="text-sm text-gray-600">{client.email} | {client.phone}</span>
                    </div>
                    <span className="text-xs bg-gray-200 text-gray-700 px-2 py-1 rounded">{client.status}</span>
                  </div>
                </li>
              ))}
            </ul>
          </div>

          {selectedClient && (
            <div className="card-modern">
              <h2 className="subheading-modern">🗒️ Notatki – {selectedClient.name}</h2>
              <ul className="mb-4 text-sm text-gray-700 space-y-2">
                {interactions.map(i => (
                  <li key={i.id} className="border-b pb-1">
                    {i.note}
                    <div className="text-xs text-gray-400">({new Date(i.interaction_date).toLocaleString()})</div>
                  </li>
                ))}
              </ul>
              <textarea
                className="input-modern"
                placeholder="Dodaj nową notatkę"
                value={note}
                onChange={(e) => setNote(e.target.value)}
              />
              <button onClick={handleAddNote} className="btn-modern mt-3 w-full">💾 Zapisz notatkę</button>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;
