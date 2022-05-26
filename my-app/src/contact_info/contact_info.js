import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';
import styles from './contact.module.css';
import ContactItem from './contact_item'


export default function ContactInfo() {
    let { id } = useParams();
    const [infos, setInfo] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("/contacts/" + id)
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
                throw response;
            })
            .then(data => {
                setInfo(data);
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

    const items = infos.map(user => {
        return (
            <div>
                <ContactItem data={user} />
            </div>
        );
    });

    function handleClick() {
        alert('Call in progress !!!');
      }
    function handleClick2() {
        alert('Email send!!!');
      }

    return (

        <div>
            <ul>
                {items}
            </ul>
            <button class={styles.styled} type="button" onClick={handleClick}>Call</button>
            <button class={styles.styled2} type="button" onClick={handleClick2}>Send Email</button>

        </div>
    )
}
