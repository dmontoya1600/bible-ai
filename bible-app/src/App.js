import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import BookView from './Books';

function App() {
    return (
      <BrowserRouter>
      {/* <NavBar /> */}
      <Routes>
        <Route exact={false} path="/books/:bookName/:chapterNumber" element={<BookView/>}/>
      </Routes>
    </BrowserRouter>
    );
}

export default App;
