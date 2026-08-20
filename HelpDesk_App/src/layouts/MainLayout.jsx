import { Outlet } from "react-router-dom";

function MainLayout() {
    return (
        <div className="main-layout">
            <header>
                <h1>HelpDesk</h1>
            </header>

            <div className="main-content">
                <aside>
                    Sidebar
                </aside>

                <main>
                    <Outlet />
                </main>
            </div>
        </div>
    );

}

export default MainLayout;