import React from 'react'
import styles from './contact.module.css';

export default function ContactItem(props) {
    
    return (
        <div className={styles.container}>
            <img src={props.data.picture} />
            <div className={styles.info}>
                <span className={styles.label}>{props.data.lastname}, {props.data.firstname}</span>
                <span className={styles.rating}>Number: {props.data.number}</span>
                <span className={styles.rating}>Email: {props.data.email}</span>
            </div>
        </div>
    )
}