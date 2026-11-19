import { Metadata } from "next";
import { ReactNode } from "react";

export const metadata: Metadata = {
  title: "Sweet Gourmet | Admin Studio",
  description: "Sweet Gourmet Admin Studio - Manage your e-commerce platform with ease.",
};

const RootLayout = ({ children }: { children: ReactNode }) => {
  return <>{children}</>;
};

export default RootLayout;
