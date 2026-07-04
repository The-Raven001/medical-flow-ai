export function CreatePatient() {

    return (
        <div className="flex flex-col items-center items-center">
            <h1>Register patient</h1>
            <form className="flex flex-col mt-20 gap-4">
                <input type="text"
                placeholder="first name"
                className="border p-2 rounded"
                required/>

                <input type="text"
                placeholder="last name"
                className=" border p-2 rounded"
                required />

                <input type="date"
                className="border p-2 rounded"
                required
                />

                <input type="text"
                placeholder="gender"
                className="border p-2 rounded"
                required />

                <input type="text"
                placeholder="phone number"
                className="border p-2 rounded"
                required />

                <input type="text"
                placeholder="address"
                className="border p-2 rounded"
                required />

                <input type="text"
                placeholder="preferred language" 
                className="border p-2 rounded"
                required/>

                <input type="text" 
                placeholder="intake status"
                className="border p-2 rounded"
                required/>

                <input type="text" 
                placeholder="emergency contact name"
                className="border p-2 rounded"
                required/>

                <input type="text" 
                placeholder="emergency contact phone number"
                className="border p-2 rounded"
                required/>

                <input type="text"
                placeholder="insurance provider"
                className="border p-2 rounded"
                required 
                />

                <input type="text"
                placeholder="insurance id"
                className="border p-2 rounded"
                required />
            </form>
        </div>
    )
}