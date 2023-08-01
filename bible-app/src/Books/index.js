import React, { useState, useEffect } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import axios from 'axios';

function BookView() {
    const [chapter, setChapter] = useState(null);
    const [verses, setVerses] = useState(null);
    let { bookName, chapterNumber } = useParams();

    console.log('BOOK NAME:', bookName);
    console.log('Chapter Number:', chapterNumber);
    console.log('chapter Data:', chapter)
    useEffect(() => {
        axios.get(`http://localhost:8000/books/${bookName}/${chapterNumber}`)
            .then(response => {
                setChapter(response.data);
                setVerses(response.data.verses)
            })
            .catch(error => {
                console.error('Error fetching data: ', error);
            })
    }, []);

    if(!chapter) return "No Book!";
    function mappingForVerses() {
        return verses.map((verse, index) => {
            return (
                <div key={index}>
                    <h3>{verse.number}</h3>
                    <p>{verse.text}</p>
                </div>
            )
        })
    }

    function getNextChapterUrl() {
        let nextChapter = parseInt(chapterNumber) + 1;
        return `/books/${bookName}/${nextChapter}`;
    }

    function nextChapter() {
      if (chapter.book.number_of_chapters <= chapterNumber) return;
      const nextChapterUrl = getNextChapterUrl();
      console.log('nextChapterUrl:', nextChapterUrl);
      window.location.replace(`http://localhost:3000${nextChapterUrl}`);
    }

    function getPreviousChapterUrl() {
        let previousChapter = parseInt(chapterNumber) - 1;
        return `/books/${bookName}/${previousChapter}`;
    }

    function previousChapter() {
      if (parseInt(chapterNumber) === 1) return;
      const previousChapterUrl = getPreviousChapterUrl();
      console.log('previousChapterUrl:', previousChapterUrl);
      window.location.replace(`http://localhost:3000${previousChapterUrl}`);
    }
    return (
        <div>
            <button onClick={previousChapter}>Previous Chapter</button>
            <button onClick={nextChapter}>Next Chapter</button>
            <h1>{bookName}</h1>
            <h2>Chapter {chapterNumber}</h2>
            {mappingForVerses()}

        </div>
    );
}

export default BookView;
