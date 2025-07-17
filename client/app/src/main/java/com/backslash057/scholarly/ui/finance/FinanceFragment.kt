package com.backslash057.scholarly.ui.finance

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import com.backslash057.scholarly.databinding.FragmentFinanceBinding

class FinanceFragment : Fragment() {

    private var _binding: FragmentFinanceBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val FinanceViewModel =
            ViewModelProvider(this).get(FinanceViewModel::class.java)

        _binding = FragmentFinanceBinding.inflate(inflater, container, false)
        val root: View = binding.root

        val textView: TextView = binding.textFinance
        FinanceViewModel.text.observe(viewLifecycleOwner) {
            textView.text = it
        }
        return root
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}