import React, { useState, useEffect } from 'react'
import ContactItem from './contact_item'
import { Link } from "react-router-dom"

export default function ContactList() {
    const [contacts, setContacts] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("/contacts")
            .then(response => {
                if (response.ok){
                    return response.json()
                }
                throw response;
            })
            .then(data => {
                setContacts(data);
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
                setError(error);
            })
            .finally(() => {
                setLoading(false);
            })
    }, []);

    if (loading) return "Loading ...";
    if (error) return "Error!";
     
    const items = contacts.map(user => {
        const id = user.id;
        const route = "/contacts/" + id;
        return (
            <li>
                <Link to={route}><ContactItem data={user} /></Link>
            </li>
        );
    });

    return (
        <div>
            <ul>
                {items}
            </ul>
        </div>
    )
}