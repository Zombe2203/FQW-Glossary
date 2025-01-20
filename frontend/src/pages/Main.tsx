import React, { FC, useEffect, useState } from 'react';
import { Navigate, Route, Routes } from "react-router-dom";

import { Header } from '../components/molecules/Header/Header';
import { Card } from '../components/atoms/Card/Card';
import { Graf } from '../components/molecules/Graf/Graf';

import { IGlossaryItem } from '../interfaces/glossary-item.interface';
import { ILink } from '../interfaces/link.interface';

import './Main.css';

export const Main: FC = () => {

  const [data, setData] = useState<IGlossaryItem[]>([])

  useEffect(() => {
    async function fetchDocuments() {
      try {
        const response = await fetch('http://localhost:8500/fullGlossary');
        if (!response.ok) {
          throw new Error('Failed to fetch documents');
        }
        const data = await response.json();
        setData(data);
        console.log(data)
      } catch (err) {
        console.log('ERROR DURING DATA RECIEVE')
      } finally {
        console.log('FINALLY!')
      }
    }

    fetchDocuments();
  }, []);

  // Создаем мапу { concept: id }
  const conceptToIdMap = Object.fromEntries(data.map(item => [item.concept, item.id]));

  // Формируем массив связей
  const relations = data.flatMap(parent =>
    parent.childConcepts?.map(child => ({
      target: parent.id,
      source: conceptToIdMap[child.child] || '',
      relation: child.connector
    }))
  );

  console.log(relations);

  return (
    <div className="mainContainer">
      <Header />

      <Routes>
        <Route
          path="/glossary"
          element={
            <div className="content-area">
              {data.map(notion => <Card id={notion.id} concept={notion.concept} definition={notion.definition} source={notion.source} />)}
            </div>
          }
        />

        <Route
          path="/semantic-graph"
          element={
            <div className="content-area">
              <Graf concepts={data} relations={relations as ILink[]} />
            </div>
          }
        />

        <Route
          path="/*"
          element={
            <Navigate to="/glossary" />
          } />
      </Routes>
    </div>
  );
}