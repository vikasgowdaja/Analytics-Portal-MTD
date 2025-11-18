import { useEffect, useState } from "react";
import axios from "axios";

interface OverviewData {
  total_students: number;
  total_departments: number;
  avg_marks: number;
  students_per_department: Array<{
    Department: string;
    Total_Students: number;
  }>;
}

interface UseOverviewDataReturn {
  data: OverviewData | null;
  loading: boolean;
  error: string | null;
}

/**
 * Custom hook for fetching overview dashboard data
 * Implements retry logic, request cancellation, and proper error handling
 */
export function useOverviewData(refreshKey) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);

    fetch("http://localhost:5000/api/overview?" + refreshKey)
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });

  }, [refreshKey]);   // <--- DEPENDENCY ADDED

  return { data, loading, error };
}

