import React from "react";
import { Link, useLocation } from "react-router-dom";

import "./Header.css"

export const Header: React.FC = () => {

  const { pathname } = useLocation();

  return (
    <header className="headerContainer">
      <div className="navigation-logo-avatar-area">
        <div className="navigation-avatar" >
          Mikhail Fatov: Glossary
        </div>
      </div>

      <div className="navigation-button-area">
        <Link to="/glossary" className="navigation-link">
          <div className={`navigation-button ${pathname === "/glossary" ? "navigation-button-selected" : ""}`}>
            Глоссарий
          </div>
        </Link>

        <Link to="/semantic-graph" className="navigation-link">
          <div className={`navigation-button ${pathname === "/semantic-graph" ? "navigation-button-selected" : ""}`}>
            Семантический граф
          </div>
        </Link>
      </div>

    </header>
  );
}